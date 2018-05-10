let dom = {
    getModal(event) {
        let url = this.dataset.url;
        let modal = document.getElementById('modal');
        let span = document.getElementsByClassName("close")[0];

        modal.style.display = "block"
        span.onclick = function () {
            modal.style.display = "none";
        }

        function reqListener() {
            if (request.status < 400) { // successful response
                let responseData = JSON.parse(this.response).residents;
                console.log(responseData);
            }
        }

        let request = new XMLHttpRequest();
        request.addEventListener('load', reqListener);
        request.open('GET', url);
        request.send();


    },
    initialize() {
        let buttons = document.getElementsByClassName('details');

        [].forEach.call(buttons, function (button) {
            button.addEventListener("click", dom.getModal);
        });
        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    }
}

dom.initialize();