var cookiesDiv = document.querySelector("#cookies")

function accept() {
    cookiesDiv.remove();
}

var fileInput = document.getElementById('file');
var fileList = [];

fileInput.addEventListener('change', function (evnt) { 
    fileList = [];
    for (var i = 0; i < fileInput.files.length; i++) {
        fileList.push(fileInput.files[i]);
        }
    }
);

var fileCatcher = document.getElementById('file');

fileCatcher.addEventListener('submit', function (evnt) {
    evnt.preventDefault();
    fileList.forEach(function (file) {
        sendFile(file);
        });
    }
);