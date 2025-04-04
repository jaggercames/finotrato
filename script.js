function findDogTag() {
    let dogTagId = document.getElementById('dogtagname').value.trim();

    if (!dogTagId) {
        alert("Por favor, insira um ID válido!");
        return;
    }

    fetch(`http://127.0.0.1:5000/find_dog?id=${encodeURIComponent(dogTagId)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("ID não encontrado!");
            }
            return response.json();
        })
        .then(data => {
            // Codifica os valores para evitar problemas na URL
            let params = new URLSearchParams();
            Object.keys(data).forEach(key => {
                params.append(key, encodeURIComponent(data[key]));
            });

            window.location.href = `dogshow.html?${params.toString()}`;
        })
        .catch(error => {
            alert(error.message);
        });
}
