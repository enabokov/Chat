import $ from 'jquery';

function getCachedMessages() {
  $.ajax({
    url: '/message/cached',
    method: 'POST',
    async: true,
    contentType: 'application/json; charset=utf-8',
    success: function (data) {
      let parsed = JSON.parse(data.toString());
      for (let i = 0; i < parsed.length; i++) {
        let _data = parsed[i];
        sendMessage(_data.name, _data.time, _data.message)
      }
    },
    error: function (data) {}
  });
}

function getCurrentMessages() {
  $.ajax({
    url: '/message/current',
    method: 'POST',
    async: true,
    contentType: 'application/json; charset=utf-8',
    success: function (data) {
      let parsed = JSON.parse(data.toString());
      let messages = parsed.messages;
      let username = parsed.user;
      for (let i = 0; i < messages.length; i++) {
        let _data = messages[i];
        console.log(_data);
        if (_data.name.toLowerCase() !== username.toLowerCase()) {
          sendMessage(_data.name, _data.time, _data.message)
        }
      }
    },
    error: function (data) {}
  });
}

$(function () {
  let href = document.location.href;
  if (href.endsWith('chat')) {
    getCachedMessages();
  }
});


setInterval(function() {
  let href = document.location.href;
  if (href.endsWith('chat')) {
    getCurrentMessages();
  }
}, 1000);


function getMessage(remove=false) {
  let selector = $('input')[0];
  let msg = selector.value;
  if (remove) {
    selector.value = "";
  }
  msg.trim();
  return msg;
}


function sendMessage(name, time, msg) {
  if (msg !== null) {
    let chat_box = $('#chat_box');
    chat_box.append('<p>(' + time + ') ' + name + ': ->  ' + msg + '</p>');
    chat_box.animate({
      scrollTop: chat_box[0].scrollHeight
    }, 1)
  }
}


function postRequest() {
  $.ajax({
    url: '/message',
    method: 'POST',
    async: true,
    data: JSON.stringify({ 'message': getMessage(true)}),
    contentType: 'application/json; charset=utf-8',
    success: function (data) {
      let parsed = JSON.parse(data.toString());
      sendMessage(parsed.name, parsed.time, parsed.message);
    },
    error: function (data) {}
  });
}


$(() => {
    $('.send_message')
      .on('keypress', function (event) {
        if (event.which === 13) {
            event.preventDefault();
            postRequest();
        }
      })
      .on('click', function (event) {
        event.preventDefault();
        if (this.tagName === 'BUTTON') {
          postRequest();
        }
      });
});