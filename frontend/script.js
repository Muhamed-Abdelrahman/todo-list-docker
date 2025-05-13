document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = '/static/login.html';
    } else {
        fetchTasks();
    }

    document.getElementById('task-form').addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        try {
            const response = await fetch('/tasks', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({ title, description })
            });
            if (response.ok) {
                document.getElementById('task-form').reset();
                fetchTasks();
            } else {
                const data = await response.json();
                alert(data.detail);
            }
        } catch (error) {
            alert('Error adding task');
        }
    });
});

async function fetchTasks() {
    const token = localStorage.getItem('token');
    try {
        const response = await fetch('/tasks', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        if (response.ok) {
            const tasks = await response.json();
            const taskList = document.getElementById('task-list');
            taskList.innerHTML = '';
            tasks.forEach(task => {
                const li = document.createElement('li');
                li.innerHTML = `<strong>${task.title}</strong>: ${task.description} <button onclick="deleteTask(${task.id})">Delete</button>`;
                taskList.appendChild(li);
            });
        } else {
            const data = await response.json();
            alert(data.detail);
        }
    } catch (error) {
        alert('Error fetching tasks');
    }
}

async function deleteTask(taskId) {
    const token = localStorage.getItem('token');
    try {
        const response = await fetch(`/tasks/${taskId}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        if (response.ok) {
            fetchTasks();
        } else {
            const data = await response.json();
            alert(data.detail);
        }
    } catch (error) {
        alert('Error deleting task');
    }
}

function logout() {
    localStorage.removeItem('token');
    window.location.href = '/static/login.html';
}
