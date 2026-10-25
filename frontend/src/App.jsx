
import { NavLink, Route, Routes } from "react-router-dom";
import WarrantyList from "./pages/WarrantyList";
import WarrantyDetail from "./pages/WarrantyDetail";
import WarrantyCreate from "./pages/WarrantyCreate";
import "./App.css";

export default function App() {
  return (
    <div className="app-shell">
      <header className="topbar">
        <div>
          <h1>MEKONG MOBILE</h1>
          <p>Smart CRM · Quản lý bảo hành</p>
        </div>
      </header>

      <nav className="navigation">
        <NavLink to="/">Danh sách phiếu</NavLink>
        <NavLink to="/tiep-nhan">Tiếp nhận bảo hành</NavLink>
      </nav>

      <main className="main-content">
        <Routes>
          <Route path="/" element={<WarrantyList />} />
          <Route path="/tiep-nhan" element={<WarrantyCreate />} />
          <Route path="/phieu/:id" element={<WarrantyDetail />} />
          <Route path="*" element={<p>Không tìm thấy trang.</p>} />
        </Routes>
      </main>

      <footer>Smart CRM — Mekong Mobile · Track SE</footer>
    </div>
  );
}
