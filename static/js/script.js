console.log("JavaScript Connected");

document.addEventListener(('DOMContentLoaded'), () => {
	const dialog = document.querySelector('#logout-dialog');
	const openDialogButton = document.querySelector('#logout-btn');
	const closeDialogButton = document.querySelector('#closeLogoutDialog');

	if(openDialogButton){
		openDialogButton.addEventListener('click', (e) => {
			e.preventDefault();
			dialog.showModal();
		});
	}

	closeDialogButton.addEventListener('click', (e) => {
		e.preventDefault();
		dialog.close();
	});
});



// ----------- Loader ----------------//
window.onload = function() {
    var loader = document.querySelector('.loader-page');
    loader.style.display = 'none';
};