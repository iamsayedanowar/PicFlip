const dropZone = document.getElementById("drop-zone");
const fileInput = document.getElementById("file-input");
const filePreview = document.getElementById("file-preview");
const fileName = document.getElementById("file-name");
const fileSize = document.getElementById("file-size");

dropZone.addEventListener("dragover", (e) => {
    e.preventDefault();
    dropZone.classList.add("dragover");
});

dropZone.addEventListener("dragleave", () => {
    dropZone.classList.remove("dragover");
});

dropZone.addEventListener("drop", (e) => {
    e.preventDefault();
    dropZone.classList.remove("dragover");
    const files = e.dataTransfer.files;
    if (files.length) {
        fileInput.files = files;
        showFileInfo(files[0]);
    }
});

fileInput.addEventListener("change", () => {
    if (fileInput.files.length > 0) {
        showFileInfo(fileInput.files[0]);
    }
});

function showFileInfo(file) {
    const maxLength = 16;
    const fullName = file.name;
    const dotIndex = fullName.lastIndexOf(".");
    const namePart = dotIndex !== -1 ? fullName.substring(0, dotIndex) : fullName;
    const extPart = dotIndex !== -1 ? fullName.substring(dotIndex) : "";
    let truncatedName = namePart;
    if (namePart.length > maxLength) {
        truncatedName = namePart.substring(0, maxLength - 3) + "...";
    }
    fileName.textContent = truncatedName + extPart;
    fileName.title = fullName;
    fileSize.textContent = `${(file.size / (1024 * 1024)).toFixed(2)} MBs`;
    filePreview.style.display = "inline-flex";
}