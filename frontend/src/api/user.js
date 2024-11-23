import { useHttp } from "@/composables/useHttp";

export default class UserApi {
    // User endpoints
    async getAllUsers() {
        return useHttp('/v1/user/', "GET");
    }

    async createUser(data) {
        return useHttp(`/v1/user/`, 'POST', data);
    }

    async getUser(id) {
        return useHttp(`/v1/user/${id}`, "GET");
    }

    async updateUser(id, data) {
        return useHttp(`/v1/user/${id}`, 'PUT', data);
    }

    async deleteUser(id) {
        return useHttp(`/v1/user/${id}`, 'DELETE');
    }

    async createGuest() {
        return useHttp(`/v1/user/guest`, 'POST');
    }
}