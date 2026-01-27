const serverUrl = 'http://127.0.0.1:5000';

export async function get_recomendations() {
  try {
    const response = await fetch(serverUrl + '/recomendations');
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
    const response = await fetch(serverUrl + '/playlists');
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
    const response = await fetch(serverUrl + '/openPlaylist', {
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
    const response = await fetch(serverUrl + '/swap', {
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
//* ich glaube swap ist nicht so der way to go ich kann ja nicht automatisch neue accounts erstellen
//! idee: datenbank und ich habe mehrere user welche abonierte kanäle haben und playlists was dann alles
//! über einen user läuft
