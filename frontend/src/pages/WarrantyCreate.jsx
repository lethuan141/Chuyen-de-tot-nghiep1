
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { api } from "../api/client";

export default function WarrantyCreate() {
  const navigate = useNavigate();

  const [phone, setPhone] = useState("");
  const [customer, setCustomer] = useState(null);
  const [customerName, setCustomerName] = useState("");

  const [serial, setSerial] = useState("");
  const [device, setDevice] = useState(null);

  const [description, setDescription] = useState("");
  const [category, setCategory] = useState("HARDWARE");
  const [priority, setPriority] = useState("CAO");

  const [message, setMessage] = useState("");
  const [error, setError] = useState("");
  const [busy, setBusy] = useState(false);

  async function lookupCustomer() {
    setCustomer(null);
    setError("");
    setMessage("");

    if (!phone.trim()) {
      setError("Vui lòng nhập số điện thoại.");
      return;
    }

    try {
      const result = await api.getCustomerByPhone(phone.trim());

      if (!result) {
        setMessage("Chưa tìm thấy khách hàng. Bạn có thể tạo hồ sơ mới.");
        return;
      }

      setCustomer(result);
      setMessage("Đã tìm thấy khách hàng.");
    } catch (err) {
      if (
        err.message.includes("404") ||
        err.message.toLowerCase().includes("not found")
      ) {
        setMessage("Chưa tìm thấy khách hàng. Bạn có thể tạo hồ sơ mới.");
      } else {
        setError(err.message || "Không thể tra cứu khách hàng.");
      }
    }
  }

  async function createCustomer() {
    setError("");
    setMessage("");

    if (!customerName.trim() || !phone.trim()) {
      setError("Vui lòng nhập họ tên và số điện thoại.");
      return;
    }

    try {
      const result = await api.createCustomer({
        customer_name: customerName.trim(),
        phone: phone.trim(),
      });

      setCustomer(result);
      setMessage("Đã tạo hồ sơ khách hàng.");
    } catch (err) {
      setError(err.message || "Không thể tạo khách hàng.");
    }
  }

  async function lookupDevice() {
    setDevice(null);
    setError("");
    setMessage("");

    if (!serial.trim()) {
      setError("Vui lòng nhập Serial/IMEI.");
      return;
    }

    try {
      const result = await api.getDeviceBySerial(serial.trim());

      if (!result) {
        setMessage("Không tìm thấy thiết bị với Serial/IMEI này.");
        return;
      }

      setDevice(result);
      setMessage("Đã tìm thấy thiết bị.");
    } catch (err) {
      setError(err.message || "Không thể tra cứu thiết bị.");
    }
  }

  async function submitTicket(event) {
    event.preventDefault();
    setError("");
    setMessage("");

    const rawCustomerId =
      customer?.customer_id ?? customer?.id;

    const rawDeviceId =
      device?.device_id ?? device?.id;

    const customerId = Number(rawCustomerId);
    const deviceId = Number(rawDeviceId);

    if (
      rawCustomerId == null ||
      rawDeviceId == null ||
      !Number.isInteger(customerId) ||
      customerId <= 0 ||
      !Number.isInteger(deviceId) ||
      deviceId <= 0
    ) {
      setError(
        "Vui lòng tra cứu lại khách hàng và thiết bị hợp lệ trước khi tạo phiếu."
      );
      return;
    }

    if (!description.trim()) {
      setError("Vui lòng nhập mô tả sự cố.");
      return;
    }

    setBusy(true);

    try {
      const result = await api.createTicket({
        customer_id: customerId,
        device_id: deviceId,
        issue_description: description.trim(),
        issue_category: category,
        priority,
      });

      if (!result?.ticket_id) {
        throw new Error("API không trả về mã phiếu bảo hành.");
      }

      navigate(`/phieu/${encodeURIComponent(result.ticket_id)}`);
    } catch (err) {
      setError(err.message || "Không thể tạo phiếu bảo hành.");
    } finally {
      setBusy(false);
    }
  }

  const customerCode =
    customer?.customer_code ??
    (typeof customer?.customer_id === "string" &&
    customer.customer_id.startsWith("CUS")
      ? customer.customer_id
      : null);

  return (
    <section>
      <div className="page-heading">
        <div>
          <h2>Tiếp nhận bảo hành</h2>
          <p>Tra cứu khách hàng, thiết bị và lập phiếu mới.</p>
        </div>
      </div>

      {error && (
        <div className="notice error" role="alert">
          {error}
        </div>
      )}

      {message && (
        <div className="notice" role="status">
          {message}
        </div>
      )}

      <div className="form-card">
        <h3>1. Khách hàng</h3>

        <div className="form-row">
          <label>
            Số điện thoại
            <input
              type="tel"
              value={phone}
              onChange={(event) => {
                setPhone(event.target.value);
                setCustomer(null);
                setMessage("");
                setError("");
              }}
              placeholder="Nhập số điện thoại"
              required
            />
          </label>

          <button
            type="button"
            className="secondary-button"
            onClick={lookupCustomer}
          >
            Tra cứu
          </button>
        </div>

        {customer && (
          <p className="success-text">
            Khách hàng:{" "}
            {customer.customer_name || customer.name || "Đã xác nhận"}
            {" — "}
            Mã:{" "}
            {customerCode ||
              customer.customer_id ||
              customer.id ||
              "Chưa có mã"}
          </p>
        )}

        {!customer &&
          message.includes("Chưa tìm thấy khách hàng") && (
            <div className="form-row">
              <label>
                Họ tên khách hàng mới
                <input
                  value={customerName}
                  onChange={(event) =>
                    setCustomerName(event.target.value)
                  }
                  placeholder="Nhập họ tên"
                />
              </label>

              <button
                type="button"
                className="secondary-button"
                onClick={createCustomer}
              >
                Tạo khách hàng
              </button>
            </div>
          )}

        <hr />

        <h3>2. Thiết bị</h3>

        <div className="form-row">
          <label>
            Serial/IMEI
            <input
              value={serial}
              onChange={(event) => {
                setSerial(event.target.value);
                setDevice(null);
                setMessage("");
                setError("");
              }}
              placeholder="Ví dụ: IMEI123456789"
              required
            />
          </label>

          <button
            type="button"
            className="secondary-button"
            onClick={lookupDevice}
          >
            Tra cứu thiết bị
          </button>
        </div>

        {device && (
          <p className="success-text">
            Đã xác nhận thiết bị — ID:{" "}
            {device.device_id ?? device.id}
            {device.device_type
              ? ` — ${device.device_type}`
              : ""}
            {device.brand ? ` ${device.brand}` : ""}
            {device.model ? ` ${device.model}` : ""}
          </p>
        )}

        <hr />

        <form onSubmit={submitTicket}>
          <h3>3. Thông tin lỗi</h3>

          <label>
            Mô tả sự cố
            <textarea
              value={description}
              onChange={(event) =>
                setDescription(event.target.value)
              }
              minLength={1}
              required
              placeholder="Mô tả lỗi khách hàng gặp phải"
            />
          </label>

          <div className="form-row">
            <label>
              Nhóm lỗi
              <select
                value={category}
                onChange={(event) =>
                  setCategory(event.target.value)
                }
              >
                <option value="HARDWARE">
                  HARDWARE — Phần cứng
                </option>
                <option value="SOFTWARE">
                  SOFTWARE — Phần mềm
                </option>
                <option value="COSMETIC">
                  COSMETIC — Ngoại quan
                </option>
                <option value="POWER">
                  POWER — Nguồn điện
                </option>
              </select>
            </label>

            <label>
              Mức ưu tiên
              <select
                value={priority}
                onChange={(event) =>
                  setPriority(event.target.value)
                }
              >
                <option value="THAP">Thấp</option>
                <option value="TRUNG_BINH">Bình thường</option>
                <option value="CAO">Cao</option>
              </select>
            </label>
          </div>

          <button
            type="submit"
            className="primary-button"
            disabled={busy}
          >
            {busy ? "Đang tạo phiếu..." : "Tạo phiếu bảo hành"}
          </button>
        </form>
      </div>
    </section>
  );
}
