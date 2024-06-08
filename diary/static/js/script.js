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