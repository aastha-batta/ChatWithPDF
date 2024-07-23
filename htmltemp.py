css = '''
<style>
.chat-message {
  padding: 1.5rem;
  border-radius: 0.5rem;
  margin-bottom: 1rem;
  display: flex;
  background-color: #1F1F2E; /* Darker color */
}

.chat-message.user {
  align-items: flex-end;
  background-color: #2b313e;
}

.chat-message.bot {
  background-color: #475063;
}

.chat-message .avatar {
  width: 20%;
}

.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}

.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #ffffff; /* White text for better visibility */
}

@media (max-width: 768px) {
  .chat-message {
    flex-direction: column;
  }
  .chat-message .avatar {
    width: 100%;
    margin-bottom: 1rem;
  }
  .chat-message .message {
    width: 100%;
  }
}
</style>

'''

bot_template = '''
<div class="chat-message bot">
  <div class="avatar">
    <img src="https://cdn-icons-png.flaticon.com/512/6134/6134346.png" alt="Bot Avatar">
  </div>
  <div class="message">
    <span class="username">Bot:</span> {{MSG}}
  </div>
</div>
'''

user_template = '''
<div class="chat-message user">
  <div class="message">
    <span class="username">User:</span> {{MSG}}
  </div>
  <div class="avatar">
    <img src="https://png.pngtree.com/png-vector/20190321/ourmid/pngtree-vector-users-icon-png-image_856952.jpg" alt="User Avatar">
  </div>
</div>
'''
