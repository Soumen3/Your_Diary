

document.addEventListener(('DOMContentLoaded'), () => {
	const dialog = document.querySelector('#delete-account-dialog');
	const openDialogButton = document.querySelector('#delete-account');
	const closeDialogButton = document.querySelector('#closeDialog');

	openDialogButton && openDialogButton.addEventListener('click', (e) => {
		e.preventDefault();
		dialog.showModal();
	});

	closeDialogButton.addEventListener('click', (e) => {
		e.preventDefault();
		dialog.close();
	});
});