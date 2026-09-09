// Fetch and display challenges
function loadChallenges() {
    fetch('/api/challenges')
        .then(response => response.json())
        .then(data => {
            const grid = document.getElementById('challenges-grid');
            grid.innerHTML = '';
            data.challenges.forEach(challenge => {
                const card = document.createElement('div');
                card.className = 'challenge-card';
                card.innerHTML = `
                    <h3>${challenge.title}</h3>
                    <p>${challenge.description}</p>
                    <div class="difficulty ${challenge.difficulty.toLowerCase()}">
                        ${challenge.difficulty}
                    </div>
                    <div class="points">Points: ${challenge.points}</div>
                `;
                card.onclick = () => loadChallengeDetail(challenge.id);
                grid.appendChild(card);
            });
        })
        .catch(error => console.error('Error loading challenges:', error));
}

// Load challenge detail
function loadChallengeDetail(challengeId) {
    fetch(`/api/challenges/${challengeId}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('challenges-grid').parentElement.parentElement.style.display = 'none';
            const detailSection = document.getElementById('challenge-detail');
            detailSection.style.display = 'block';
            
            const content = document.getElementById('detail-content');
            content.innerHTML = `
                <h3>${data.title}</h3>
                <p><strong>Description:</strong> ${data.description}</p>
                <h4>Challenge:</h4>
                <p>${data.content}</p>
                <h4>Task:</h4>
                <p>${data.task}</p>
                <div style="background: #1a1a2e; padding: 1rem; border-radius: 5px; margin-top: 1rem;">
                    <p><strong>Submit your flag:</strong></p>
                    <input type="text" id="flag-input" class="flag-input" placeholder="FLAG{...}">
                    <button class="btn btn-submit" onclick="submitFlag(${challengeId})">Submit Flag</button>
                    <div id="flag-message"></div>
                </div>
            `;
        })
        .catch(error => console.error('Error loading challenge:', error));
}

// Submit flag
function submitFlag(challengeId) {
    const flag = document.getElementById('flag-input').value;
    fetch('/api/submit-flag', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ challengeId, flag })
    })
    .then(response => response.json())
    .then(data => {
        const message = document.getElementById('flag-message');
        message.className = `message ${data.success ? 'success' : 'error'}`;
        message.textContent = data.message;
    })
    .catch(error => console.error('Error submitting flag:', error));
}

// Back to challenges
function backToChallenges() {
    document.getElementById('challenge-detail').style.display = 'none';
    document.getElementById('challenges-grid').parentElement.parentElement.style.display = 'block';
}

// Scroll to section
function scrollToSection(sectionId) {
    const element = document.getElementById(sectionId);
    element.scrollIntoView({ behavior: 'smooth' });
}

// Initialize
window.addEventListener('DOMContentLoaded', loadChallenges);
