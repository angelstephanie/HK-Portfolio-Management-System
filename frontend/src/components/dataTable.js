import React, { useState, useMemo } from 'react';
import { FaSort, FaSortUp, FaSortDown, FaTimes } from 'react-icons/fa';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/dataTable.css';

const DataTable = ({ columns, data, globalFilter }) => {
  const portfolios = useMemo(() => {
    const grouped = {};
    data.forEach((item) => {
      const key = item.portfolio_id;
      if (!grouped[key]) grouped[key] = [];
      grouped[key].push(item);
    });
    return grouped;
  }, [data]);

  const portfolioIds = Object.keys(portfolios);
  const [activePortfolio, setActivePortfolio] = useState(portfolioIds[0]);
  const [sortConfig, setSortConfig] = useState(null);

  const filteredData = portfolios[activePortfolio].filter((row) =>
    Object.values(row).join(' ').toLowerCase().includes(globalFilter.toLowerCase())
  );

  const sortedData = useMemo(() => {
    if (!sortConfig) return filteredData;
    const { key, direction } = sortConfig;
    return [...filteredData].sort((a, b) => {
      const aVal = a[key];
      const bVal = b[key];
      if (aVal < bVal) return direction === 'asc' ? -1 : 1;
      if (aVal > bVal) return direction === 'asc' ? 1 : -1;
      return 0;
    });
  }, [filteredData, sortConfig]);

  const handleSort = (key) => {
    setSortConfig((prev) => {
      if (!prev || prev.key !== key) return { key, direction: 'asc' };
      return {
        key,
        direction: prev.direction === 'asc' ? 'desc' : 'asc',
      };
    });
  };

  const renderSortIcon = (key) => {
    if (!sortConfig || sortConfig.key !== key) return <FaSort />;
    return sortConfig.direction === 'asc' ? <FaSortUp /> : <FaSortDown />;
  };

  const columnGridStyle = {
    gridTemplateColumns: `repeat(${columns.length}, minmax(150px, 1fr))`,
  };

  return (
    <div className="container-fluid">
      <ul className="nav nav-tabs mb-3">
        {portfolioIds.map((id, index) => (
          <li className="nav-item" key={id}>
            <button
              className={`nav-link ${activePortfolio === id ? 'active' : ''}`}
              onClick={() => {
                setActivePortfolio(id);
                setSortConfig(null);
              }}
              type="button"
            >
              Portfolio {index + 1}
            </button>
          </li>
        ))}
      </ul>
      <div className="table-wrapper">
        <div className="table-grid" style={columnGridStyle}>
          {columns.map((col) => (
            <div
              key={col.accessor}
              className="header-cell"
              onClick={() => handleSort(col.accessor)}
            >
              <span>{col.header}</span>
              <span className="ms-2">{renderSortIcon(col.accessor)}</span>
              {sortConfig && sortConfig.key === col.accessor && (
                <button
                  className="clear-sort-icon"
                  onClick={(e) => {
                    e.stopPropagation();
                    setSortConfig(null);
                  }}
                  title="Clear sorting"
                  aria-label={`Clear sorting on ${col.header}`}
                  type="button"
                >
                  <FaTimes />
                </button>
              )}
            </div>
          ))}

          {sortedData.length === 0 ? (
            <p className="text-center text-muted py-3" style={{ gridColumn: `span ${columns.length}` }}>
              No data available
            </p>
          ) : (
            sortedData.map((row, idx) => (
              <div key={idx} className="row-card" style={{ gridColumn: `span ${columns.length}` }}>
                <div className="row-card-grid" style={columnGridStyle}>
                  {columns.map((col) => (
                    <div key={col.accessor} className="row-cell">
                      {row[col.accessor]}
                    </div>
                  ))}
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default DataTable;
