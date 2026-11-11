import axios, { AxiosResponse } from 'axios';

const API_URL = import.meta.env.VITE_BACKEND_URL || 'http://localhost:8000';

interface GenerationResponse {
  success: boolean;
  result: string;
  generation_id: number;
}

export const aiService = {
  generateText: async (prompt: string): Promise<GenerationResponse> => {
    const response: AxiosResponse<GenerationResponse> = await axios.post(
      `${API_URL}/api/v1/ai/generate/text`, 
      { prompt }
    );
    return response.data;
  },
  
  generateImage: async (prompt: string): Promise<GenerationResponse> => {
    const response: AxiosResponse<GenerationResponse> = await axios.post(
      `${API_URL}/api/v1/ai/generate/image`, 
      { prompt }
    );
    return response.data;
  },
  
  generateVoice: async (text: string): Promise<Blob> => {
    const response: AxiosResponse<Blob> = await axios.post(
      `${API_URL}/api/v1/ai/generate/voice`,
      { text },
      { responseType: 'blob' }
    );
    return response.data;
  }
}; 