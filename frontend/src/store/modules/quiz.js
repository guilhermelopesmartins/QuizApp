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
      quizDisplay: null,
      selectedDifficulty: null,
      quizzes: [],
      filterQuizzes: [],
      users: [],
    }
  },
  getters: {
    
  },
  actions: {
    getQuizStatus () {
      return this.quizStatus;
    },
    saveAnswer(data) {
      quizApi.createAnswer(data)
    },
    saveResults(data) {
      quizApi.createResult(data);
    },
    getSelectedQuiz() {
      return this.selectedQuiz;
    },
    async getAllCategories() {
      return helper.getDataFromResponse(await quizApi.getAllCategories());
    },
    sendFeedBack(data) {
      quizApi.createFeedback(data);
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
    async getAllResults () {
      return helper.getDataFromResponse(await quizApi.getAllResults());
    },
    setQuizDisplay(creation) {
      this.quizDisplay = creation;
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
      if (this.quizzes.length <= 0)
        return;
      this.filterQuizzes = this.quizzes.filter(q => q.category.name === this.selectedCategory);
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
