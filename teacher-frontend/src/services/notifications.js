import api from '../api';

export const getNotifications = async () => {
  try {
    const response = await api.get('/api/notifications/');
    return response.data;
  } catch (error) {
    console.error('Failed to fetch notifications:', error);
    throw error;
  }
};

export const markAsRead = async (notificationId) => {
  try {
    const response = await api.patch(`/api/notifications/${notificationId}/mark_read/`);
    return response.data;
  } catch (error) {
    console.error('Failed to mark notification as read:', error);
    throw error;
  }
};

export const markAllAsRead = async () => {
  try {
    const response = await api.post('/api/notifications/mark_all_read/');
    return response.data;
  } catch (error) {
    console.error('Failed to mark all notifications as read:', error);
    throw error;
  }
};
