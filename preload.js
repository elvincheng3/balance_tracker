function createSuccessAlert(successText) {
    var alert = document.createElement("div");
    alert.id = "alert"
    alert.classList.add("alert");
    alert.classList.add("alert-success");
    alert.classList.add("alert-dismissible");
    alert.classList.add("fade");
    alert.classList.add("show");
    
    var alertText = document.createElement("strong");
    alertText.innerHTML = successText;
    alert.appendChild(alertText);

    var subtitle = document.getElementById("title");
    subtitle.appendChild(alert);

    var alertButton = '<button type="button" class="close" data-dismiss="alert">&times;</button>';
    $("#alert").append(alertButton);
}

function loadPurchases() {
    $("#page").load('table_views/purchases.html');
    // createSuccessAlert("Successfully completed action");
}
function loadSales() {
    $("#page").load('table_views/sales.html');
    // createSuccessAlert("Successfully completed action");
}
function loadExpenses() {
    $("#page").load('table_views/expenses.html');
    // createSuccessAlert("Successfully completed action");
}
function loadServices() {
    $("#page").load('table_views/services.html');
    // createSuccessAlert("Successfully completed action");
}
function loadSkulist() {
    $("#page").load('table_views/skulist.html');
    // createSuccessAlert("Successfully completed action");
}

window.addEventListener('DOMContentLoaded', () => {
    loadPurchases();
});
  
window.addEventListener('load', () => {
    document.getElementById("btn-purchases").addEventListener('click', () => {
        loadPurchases();
    });
    document.getElementById("btn-sales").addEventListener('click', () => {
        loadSales();
    });
    document.getElementById("btn-expenses").addEventListener('click', () => {
        loadExpenses();
    });
    document.getElementById("btn-services").addEventListener('click', () => {
        loadServices();
    });
    document.getElementById("btn-skulist").addEventListener('click', () => {
        loadSkulist();
    });
});