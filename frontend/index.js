function openPanel() {
  console.log('hello');
  document.getElementById('topicPanel').style.display = 'block';
}
function closePanel() {
  document.getElementById('topicPanel').style.display = 'none';
}
//? remove channel function()
//? brauche wohl db when ich das auch behalten will
//? eine funktionaliy tät die den neuen button auch etwas wie onclick added oder so?
function addTopicChannel() {
  let topicChannelName = prompt('Neuer Channel:');
  if (topicChannelName) {
    let item = document.createElement('li');
    let itemBut = document.createElement('button');
    itemBut.textContent = topicChannelName;
    itemBut.id = topicChannelName.slice(0, 8);
    document.getElementById('topicList').appendChild(item);
    document.getElementById('topicList').appendChild(itemBut);
  }
}

function loadRecomendations() {}

function loadPlaylists() {}
