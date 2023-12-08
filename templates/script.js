document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("uploadForm").addEventListener("submit", function (event) {
        event.preventDefault();
    });

    document.getElementById("adjustVolumeForm").addEventListener("submit", function (event) {
        event.preventDefault();
    });
});

function uploadAudio() {
    const fileInput = document.getElementById("audioFile");
    const file = fileInput.files[0];

    const formData = new FormData();
    formData.append("audio", file);

    fetch("http://localhost:5000/api/upload", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
}

function downloadAudio() {
    fetch("http://localhost:5000/api/download")
    .then(response => response.blob())
    .then(blob => {
        const url = window.URL.createObjectURL(new Blob([blob]));
        const a = document.createElement("a");
        a.href = url;
        a.download = "downloaded_audio.wav";
        document.body.appendChild(a);
        a.click();
        window.URL.revokeObjectURL(url);
    })
    .catch(error => console.error("Error:", error));
}

function adjustVolume() {
    const volumeLevel = document.getElementById("volumeLevel").value;

    fetch("http://localhost:5000/api/adjust_volume", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            audio_file: "path/to/audiofile.wav",
            volume_level: volumeLevel
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerText = data.message;
    })
    .catch(error => console.error("Error:", error));
}
