/* eslint-disable no-console */
import { defineStore } from "pinia";

export const useQuiz = defineStore("quiz", {
  state: () => {
    return {
      categories: [],
      selectedCategory: null,
      quizStatus: null,
      selectedDifficulty: null,
      quizzes: [],
      users: [],
    }
  },
  getters: {
    
  },
  actions: { 
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
