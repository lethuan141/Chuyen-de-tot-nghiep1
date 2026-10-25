import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";
import { api } from "../api/client";
import DataState from "../components/DataState";

export default function WarrantyDetail() {
  const { id } = useParams();
  const [ticket, setTicket] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    let active = true;

    async function loadTicket() {
      setLoading(true);
      setError("");
      setTicket(null);

      try {
        const data = await api.getTicket(id);
        if (active) setTicket(data);
      } catch (err) {
        if (active) {
          setError(err.message || "Không thể tải phiếu.");
        }
      } finally {
        if (active) setLoading(false);
      }
    }

    loadTicket();

    return () => {
      active = false;
    };
  }, [id]);

  return (
    <section>
      <div className="page-heading">
        <div>
          <h2>Chi tiết phiếu bảo hành</h2>
          <p>Thông tin tiếp nhận và xử lý yêu cầu.</p>
        </div>

        <Link className="secondary-button" to="/">
          ← Quay lại
        </Link>
      </div>

      <DataState
        loading={loading}
        error={error}
        empty={!ticket && !loading && !error}
      >
        {ticket && (
          <div className="detail-card">
            <h3>{ticket.ticket_code || "Phiếu bảo hành"}</h3>

            <dl className="detail-grid">
              <dt>Mã phiếu</dt>
              <dd>{ticket.ticket_code || "—"}</dd>

              <dt>Mã khách hàng</dt>
              <dd>{ticket.customer_id ?? "—"}</dd>

              <dt>Khách hàng</dt>
              <dd>{ticket.customer_name || "—"}</dd>

              <dt>Số điện thoại</dt>
              <dd>
                {ticket.customer_phone ||
                  ticket.phone ||
                  "Chưa có dữ liệu từ API"}
              </dd>

              <dt>Mã thiết bị</dt>
              <dd>{ticket.device_id ?? "—"}</dd>

              <dt>Serial/IMEI</dt>
              <dd>{ticket.serial_number || "—"}</dd>

              <dt>Nhóm lỗi</dt>
              <dd>{ticket.issue_category || "—"}</dd>

              <dt>Mức ưu tiên</dt>
              <dd>{ticket.priority || "—"}</dd>

              <dt>Trạng thái</dt>
              <dd>{ticket.status || "—"}</dd>

              <dt>Mô tả lỗi</dt>
              <dd>{ticket.description || "—"}</dd>

              <dt>Thời gian tiếp nhận</dt>
              <dd>{ticket.received_at || "—"}</dd>

              <dt>Hạn cam kết</dt>
              <dd>{ticket.commitment_at || "—"}</dd>
            </dl>
          </div>
        )}
      </DataState>
    </section>
  );
}