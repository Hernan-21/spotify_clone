const API_URL = 'http://localhost:8080';

export const spotifyService = {
    async getUserData() {
        const response = await fetch(`${API_URL}/`);
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
    },

    async getPlaylist(playlistId) {
        const response = await fetch(`${API_URL}/playlist/${playlistId}`);
        if (!response.ok) throw new Error('Network response was not ok');
        return response.json();
    }
}; 