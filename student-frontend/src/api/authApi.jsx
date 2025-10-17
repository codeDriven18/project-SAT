import api from './index';

export const authApi = {
  // Register new student
  register: async (userData) => {
    const response = await api.post('/api/auth/register/', {
      ...userData,
      user_type: 'student'
    });
    return response.data;
  },

  // Login student
  login: async (credentials) => {
    const response = await api.post('/api/auth/login/', credentials);
    return response.data;
  },

  // Refresh token
  refreshToken: async (refreshToken) => {
    const response = await api.post('/api/auth/token/refresh/', {
      refresh: refreshToken
    });
    return response.data;
  },

  // Get current user profile (if needed)
  getProfile: async () => {
    const response = await api.get('/api/auth/profile/');
    return response.data;
  },

  // Update user profile
  updateProfile: async (profileData) => {
    const response = await api.patch('/api/auth/profile/', profileData);
    return response.data;
  },

  // Update profile picture
  updateProfilePicture: async (file) => {
    const formData = new FormData();
    formData.append('profile_picture', file);
    const response = await api.patch('/api/auth/profile/', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  }
};