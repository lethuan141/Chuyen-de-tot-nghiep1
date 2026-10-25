
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { api } from "../api/client";
import DataState from "../components/DataState";

export default function WarrantyList() {
  const [tickets, setTickets] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  async function loadTickets() {
    setLoading(true);
    setError("");

    try {
      const data = await api.getTickets();
      setTickets(Array.isArray(data) ? data : []);
    } catch (err) {
      setError(err.message || "Không thể tải danh sách phiếu.");
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadTickets();
  }, []);

  return (
    <section>
      <div className="page-heading">
        <div>
          <h2>Danh sách phiếu bảo hành</h2>
          <p>Theo dõi và tra cứu yêu cầu bảo hành của khách hàng.</p>
        </div>
        <Link className="primary-button" to="/tiep-nhan">
          + Tiếp nhận phiếu
        </Link>
      </div>

      <DataState
        loading={loading}
        error={error}
        empty={!loading && !error && tickets.length === 0}
      >
        <div className="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>Mã phiếu</th>
                <th>Khách hàng</th>
                <th>Thiết bị</th>
                <th>Loại lỗi</th>
                <th>Ưu tiên</th>
                <th>Trạng thái</th>
                <th>Hạn cam kết</th>
                <th>Chi tiết</th>
              </tr>
            </thead>
            <tbody>
              {tickets.map((ticket) => (
                <tr key={ticket.ticket_id}>
                  <td>{ticket.ticket_code}</td>
                  <td>{ticket.customer_name}</td>
                  <td>{ticket.serial_number}</td>
                  <td>{ticket.issue_category}</td>
                  <td>
                    <span className="priority">
                      {ticket.priority}
                    </span>
                  </td>
                  <td>{ticket.status}</td>
                  <td>
                    {ticket.commitment_at
                      ? new Date(ticket.commitment_at).toLocaleString("vi-VN")
                      : "Chưa xác định"}
                  </td>
                  <td>
                    <Link to={`/phieu/${ticket.ticket_id}`}>
                      Xem
                    </Link>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>

        <button className="secondary-button" onClick={loadTickets}>
          Làm mới danh sách
        </button>
      </DataState>
    </section>
  );
}
