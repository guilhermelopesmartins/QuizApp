/* eslint-disable no-console */
import { defineStore } from "pinia";
import QuizApi from "../../api/quiz";
import Helper from "../../utils/helper"

const helper = new Helper();
const quizApi = new QuizApi();

export const useQuiz = defineStore("quiz", {
  state: () => {
    return {
      categories: [],
      selectedCategory: null,
      selectedQuiz: null,
      quizStatus: null,
      quizCreation: null,
      selectedDifficulty: null,
      quizzes: [],
      users: [],
    }
  },
  getters: {
    
  },
  actions: {
    async getAllCategories() {
      return helper.getDataFromResponse(await quizApi.getAllCategories());
    },
    async createNewQuiz(quiz) {
      const data = {
        title: quiz.quiz.title,
        description: quiz.quiz.description,
        category_id: quiz.quiz.category,
        difficulty: quiz.quiz.difficulty,
        owner_id: quiz.quiz.owner_id
      };
      const newQuiz = helper.getDataFromResponse(await quizApi.createQuiz(data));
      quiz.questions.forEach(async (q) => {
        const data = {
          question_text: q.question,
          options: q.options,
          correct_answer: q.answer,
          quiz_id: newQuiz.id
        };
        await quizApi.createQuestion(data);
      });
    },
    setQuizCreation(creation) {
      this.quizCreation = creation;
    },
    setSelectedQuiz(quiz) {
      this.selectedQuiz = quiz;
    },
    setQuizzes(quizzes) {
      this.quizzes = quizzes;
    },
    setCategories(categories) {
      this.categories = categories;
    },
    setCategory(category) {
      this.selectedCategory = category;
    },
    setDifficulty(difficulty) {
      this.selectedDifficulty = difficulty;
    },
    setQuizStatus(status) {
      this.quizStatus = status;
    },
    setUsers(users){
      this.users = users;
    }
  },
})
