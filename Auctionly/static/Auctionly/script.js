const endDate = new Date("January 28, 2025 11:07:00").getTime();

    const countdownElement = document.getElementById("countdown");

    const interval = setInterval(() => {
      const now = new Date().getTime();
      const timeLeft = endDate - now;

      if (timeLeft <= 0) {
        clearInterval(interval);
        countdownElement.innerHTML = "The auction has ended.";
      } else {
        const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
        const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

        countdownElement.innerHTML = `${days}d ${hours}h ${minutes}m ${seconds}s`;
      }
    }, 1000);

let bids = [];

function placeBid() {
  const bidInput = document.getElementById("bid");
  const bidValue = parseFloat(bidInput.value.trim());
  if (!isNaN(bidValue) && bidValue > 0) {
    bids.push(bidValue);
    bids.sort((a, b) => b - a); // Sort descending
    updateBidList();
    bidInput.value = "";
  } else {
    alert("Please enter a valid positive number.");
  }
}
function updateBidList() {
  const bidList = document.getElementById("bidList");
  bidList.innerHTML = "";
  for (let i = 0; i < bids.length; i++) {
    const li = document.createElement("li");
    li.textContent = `$ Your bid is ${bids[i].toFixed(2)}`;
    bidList.appendChild(li);
  }
}