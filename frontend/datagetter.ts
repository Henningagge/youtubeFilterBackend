export async function get_recomendations() {
  try {
    const response = await fetch('http://127.0.0.1:5000/recomendations');
    if (!response.ok) {
      throw new Error(
        `Error when getting recomendations status ${response.status}`,
      );
    }
    const data = await response.json();
    return data;
  } catch (err) {
    console.error(`error: ${err}`);
  }
}
export async function get_playlists() {
  try {
    const response = await fetch('http://127.0.0.1:5000/playlists');
    if (!response.ok) {
      throw new Error(`Error when getting playlists status ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (err) {
    console.error(`error: ${err}`);
  }
}
export async function open_playlist(playlistid: string) {
  try {
    const response = await fetch('http://127.0.0.1:5000/openPlaylist', {
      method: 'GET',
      body: playlistid,
    });
    if (!response.ok) {
      throw new Error(`Error when opening playlist status ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (err) {
    console.error(`error: ${err}`);
  }
}
export async function swapChannel(channelid: string) {
  try {
    const response = await fetch('http://127.0.0.1:5000/swap', {
      method: 'GET',
      body: channelid,
    });
    if (!response.ok) {
      throw new Error(`Error when swapping channel status: ${response.status}`);
    }
    const data = await response.json();
    return data;
  } catch (err) {
    console.error(`error: ${err}`);
  }
}
