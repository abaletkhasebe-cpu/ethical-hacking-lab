const express = require('express');
const cors = require('cors');
const path = require('path');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static('public'));

// Routes
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

// API Routes
app.get('/api/challenges', (req, res) => {
  res.json({
    challenges: [
      {
        id: 1,
        title: 'SQL Injection Basics',
        description: 'Learn how SQL injection works and how to prevent it',
        difficulty: 'Beginner',
        points: 100
      },
      {
        id: 2,
        title: 'Password Cracking',
        description: 'Understanding hash functions and password security',
        difficulty: 'Intermediate',
        points: 200
      },
      {
        id: 3,
        title: 'Network Sniffing',
        description: 'Learn about packet analysis and network protocols',
        difficulty: 'Intermediate',
        points: 200
      },
      {
        id: 4,
        title: 'Cross-Site Scripting (XSS)',
        description: 'Understand XSS attacks and defense mechanisms',
        difficulty: 'Advanced',
        points: 300
      }
    ]
  });
});

app.get('/api/challenges/:id', (req, res) => {
  const challengeId = req.params.id;
  const challenges = {
    1: {
      id: 1,
      title: 'SQL Injection Basics',
      description: 'Learn how SQL injection works',
      content: 'SQL injection is when an attacker inserts SQL code into input fields...',
      task: 'Find the admin password using SQL injection in the practice form below',
      flag: 'FLAG{sql_injection_found}'
    },
    2: {
      id: 2,
      title: 'Password Cracking',
      description: 'Understanding hash functions',
      content: 'Password hashing is essential for security...',
      task: 'Crack the MD5 hash: 5d41402abc4b2a76b9719d911017c592',
      flag: 'FLAG{password_is_hello}'
    }
  };
  res.json(challenges[challengeId] || { error: 'Challenge not found' });
});

app.post('/api/submit-flag', (req, res) => {
  const { challengeId, flag } = req.body;
  const correctFlags = {
    1: 'FLAG{sql_injection_found}',
    2: 'FLAG{password_is_hello}'
  };
  
  if (correctFlags[challengeId] === flag) {
    res.json({ success: true, message: 'Correct flag! Well done!' });
  } else {
    res.json({ success: false, message: 'Incorrect flag. Try again!' });
  }
});

app.listen(PORT, () => {
  console.log(`🔒 Ethical Hacking Lab running on http://localhost:${PORT}`);
});
