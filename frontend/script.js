document.addEventListener('DOMContentLoaded', () => {
    const token = localStorage.getItem('token');
    if (!token) {
        window.location.href = '/static/login.html';
        return; // لمنع تنفيذ باقي الكود إذا لم يكن هناك token
    }

    // تعيين عناصر DOM في متغيرات
    const taskForm = document.getElementById('task-form');
    const taskList = document.getElementById('task-list');
    const titleInput = document.getElementById('title');
    const descriptionInput = document.getElementById('description');
    const logoutButton = document.querySelector('button[onclick="logout()"]');

    // تحميل المهام عند بدء التشغيل
    fetchTasks();

    // إضافة مهمة جديدة
    taskForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const title = titleInput.value.trim();
        const description = descriptionInput.value.trim();
        
        if (!title || !description) {
            alert('Please fill in all fields');
            return;
        }

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
                taskForm.reset();
                await fetchTasks();
            } else {
                const data = await response.json();
                alert(data.detail || 'Failed to add task');
            }
        } catch (error) {
            console.error('Error adding task:', error);
            alert('Error adding task');
        }
    });

    // تحسين وظيفة تسجيل الخروج
    logoutButton.addEventListener('click', logout);
});

async function fetchTasks() {
    const token = localStorage.getItem('token');
    if (!token) return;

    try {
        const response = await fetch('/tasks', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (response.ok) {
            const tasks = await response.json();
            renderTasks(tasks);
        } else {
            const data = await response.json();
            alert(data.detail || 'Failed to fetch tasks');
        }
    } catch (error) {
        console.error('Error fetching tasks:', error);
        alert('Error fetching tasks');
    }
}

function renderTasks(tasks) {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = '';
    
    if (tasks.length === 0) {
        taskList.innerHTML = '<li>No tasks found</li>';
        return;
    }

    tasks.forEach(task => {
        const li = document.createElement('li');
        li.innerHTML = `
            <div class="task-content">
                <strong>${task.title}</strong>
                <p>${task.description}</p>
            </div>
            <button onclick="deleteTask(${task.id})">Delete</button>
        `;
        taskList.appendChild(li);
    });
}

async function deleteTask(taskId) {
    const token = localStorage.getItem('token');
    if (!token) return;

    if (!confirm('Are you sure you want to delete this task?')) {
        return;
    }

    try {
        const response = await fetch(`/tasks/${taskId}`, {
            method: 'DELETE',
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });
        
        if (response.ok) {
            await fetchTasks();
        } else {
            const data = await response.json();
            alert(data.detail || 'Failed to delete task');
        }
    } catch (error) {
        console.error('Error deleting task:', error);
        alert('Error deleting task');
    }
}

function logout() {
    localStorage.removeItem('token');
    window.location.href = '/static/login.html';
}