const e = React.createElement;

function ChatApp() {
  const [messages, setMessages] = React.useState([]);
  const [input, setInput] = React.useState('');

  const sendPrompt = async () => {
    const res = await axios.post('/api/chat/', { prompt: input, session_id: 'demo' });
    setMessages([...messages, { role: 'user', text: input }, { role: 'bot', text: res.data.response }]);
    setInput('');
  };

  return e('div', null,
    messages.map((m, i) => e('div', { key: i }, `${m.role}: ${m.text}`)),
    e('input', { value: input, onChange: e => setInput(e.target.value) }),
    e('button', { onClick: sendPrompt }, 'Send')
  );
}

ReactDOM.render(e(ChatApp), document.getElementById('root'));
