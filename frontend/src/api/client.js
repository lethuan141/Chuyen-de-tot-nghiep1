
const API_BASE_URL = "http://127.0.0.1:8000";

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      "Content-Type": "application/json",
      ...options.headers,
    },
    ...options,
  });

  const text = await response.text();
  let data = null;

  try {
    data = text ? JSON.parse(text) : null;
  } catch {
    data = text;
  }

  if (!response.ok) {
    const message =
      typeof data === "object" && data !== null
        ? data.detail || `HTTP ${response.status}`
        : data || `HTTP ${response.status}`;

    throw new Error(message);
  }

  return data;
}

export const api = {
  getTickets: () => request("/api/tickets"),

  getTicket: (id) =>
    request(`/api/tickets/${encodeURIComponent(id)}`),

  createTicket: (payload) =>
    request("/api/tickets", {
      method: "POST",
      body: JSON.stringify(payload),
    }),

  getCustomerByPhone: (phone) =>
    request(`/api/customers?phone=${encodeURIComponent(phone)}`),

  createCustomer: (payload) =>
    request("/api/customers", {
      method: "POST",
      body: JSON.stringify(payload),
    }),

  getDeviceBySerial: (serialNo) =>
    request(`/api/devices?serial_no=${encodeURIComponent(serialNo)}`),
};
