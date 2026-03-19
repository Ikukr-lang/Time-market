const tg = window.Telegram.WebApp;
tg.ready();
tg.expand();

const user = tg.initDataUnsafe.user || { id: 123456, first_name: "Test" };

async function loadData() {
  document.getElementById("company-name").textContent = "Моя компания";
  document.getElementById("trial-info").textContent = "Пробный период: 7 дней";
}

async function subscribe() {
  try {
    const res = await fetch("/api/payment/create-subscription", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ telegram_id: user.id })
    });
    const data = await res.json();
    if (data.confirmation_url) {
      tg.openLink(data.confirmation_url);
    }
  } catch (e) {
    alert("Ошибка оплаты");
  }
}

loadData();
