import axios from "axios";
import { useAxios } from "@vueuse/integrations/useAxios";

export const instance = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_URL,
});

export const noAuthHTTP = axios.create({
  baseURL: import.meta.env.VITE_APP_BASE_URL,
});

export const useGenericHttp = (path, method, data = null, headers = null) => {
  const requestConfig = {
    method: method,
    headers: headers,
  };
  if (data) {
    requestConfig.data = data;
  }
  console.log(requestConfig);
  console.log(data);
  return useAxios(path, requestConfig);
};

export const useHttp = (path, method, data = null, headers = null) => {
  const requestConfig = {
    method: method,
    headers: headers,
  };
  if (data) {
    requestConfig.data = data;
  }
  return useAxios(path, requestConfig, noAuthHTTP);
};
