window.onload = () => {
    const apiUrl = "https://canary-project.onrender.com/api/logs";

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const tableBody = document.getElementById("logs-body");
            tableBody.innerHTML = "";  // Clear existing data

            if (data.length === 0) {
                tableBody.innerHTML = "<tr><td colspan='4'>No logs available</td></tr>";
            } else {
                data.forEach(log => {
                    let row = `<tr>
                        <td>${log.email_id}</td>
                        <td>${log.public_ip}</td>
                        <td>${log.user_agent}</td>
                        <td>${log.access_time}</td>
                    </tr>`;
                    tableBody.innerHTML += row;
                });
            }
        })
        .catch(error => console.error("Error fetching logs:", error));
}
