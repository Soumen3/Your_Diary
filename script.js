document.addEventListener(('DOMContentLoaded'), () => {
	const dialog = document.querySelector('#myDialog');
	const openDialogButton = document.querySelector('#openDialog');
	const closeDialogButton = document.querySelector('#closeDialog');

	openDialogButton.addEventListener('click', () => {
		dialog.showModal();
	});

	closeDialogButton.addEventListener('click', () => {
		dialog.close();
	});
})

