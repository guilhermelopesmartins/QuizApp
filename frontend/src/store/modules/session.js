/* eslint-disable no-console */
import { defineStore } from "pinia";
import UserApi from "../../api/user";
import SessionApi from "../../api/session";
import Helper from "../../utils/helper"

const userApi = new UserApi();
const sessionApi = new SessionApi();
const helper = new Helper();

export const useSession = defineStore("session", {
  state: () => {
    return {
      sessionStatus: null,
      start_time: null,
      end_time: null,
      user_id: null,
      user_name: null,
      id: null
    }
  },
  getters: {

  },
  actions: {
    getUserName() {
      return this.user_name;
    }, 
    getUserId() {
      return this.user_id;
    },
    setSessionStatus(status) {
      this.sessionStatus = status;
    },
    async createUser(user) {
      const newUser = helper.getDataFromResponse(await userApi.createUser(user));
      const now = new Date();
      const sessionObj = {
        user_id: newUser.id,
        user_name: newUser.username,
        start_time: now.toUTCString(),
        user_id: newUser.id
      };
      this.setSession(sessionObj);
      // Aqui deve criar uma sessão

      // const newSession = getData(await sessionApi.createSession(sessionObj));
      // newSession.user_name = newUser.user_name;
      // this.setSession(newSession);
    },
    setSession(session) {
      this.start_time = session.start_time;
      this.end_time = session.end_time;
      this.user_id = session.user_id;
      this.user_name = session.user_name;
    }
  },
})
