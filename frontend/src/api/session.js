import { useHttp } from "@/composables/useHttp";

export default class SessionApi {
    // Session endpoints
    async getAllSessions() {
        return useHttp('/v1/session/', "GET");
    }

    async createSession(data) {
        return useHttp(`/v1/session/`, 'POST', data);
    }

    async getSession(id) {
        return useHttp(`/v1/session/${id}`, "GET");
    }

    async updateSession(id, data) {
        return useHttp(`/v1/session/${id}`, 'PUT', data);
    }

    async deleteSession(id) {
        return useHttp(`/v1/session/${id}`, 'DELETE');
    }
}