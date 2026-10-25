
export default function DataState({
  loading = false,
  error = "",
  empty = false,
  children,
}) {
  if (loading) {
    return (
      <div className="state-message" role="status">
        Đang tải dữ liệu...
      </div>
    );
  }

  if (error) {
    return (
      <div className="state-message error" role="alert">
        <p>Không thể tải dữ liệu.</p>
        <p>{error}</p>
      </div>
    );
  }

  if (empty) {
    return (
      <div className="state-message" role="status">
        Chưa có dữ liệu.
      </div>
    );
  }

  return children;
}
