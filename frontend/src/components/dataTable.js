import React, { useState } from 'react';
import { FaSort, FaSortUp, FaSortDown, FaTimes } from 'react-icons/fa';
import '../styles/dataTable.css';

const DataTable = ({ columns, data, globalFilter }) => {
  const [sortConfig, setSortConfig] = useState(null);

  const filteredData = data.filter((row) =>
    Object.values(row)
      .join(' ')
      .toLowerCase()
      .includes(globalFilter.toLowerCase())
  );

  const sortedData = React.useMemo(() => {
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

  return (
    <div className="data-table-container">
      <div className={`header-row ${columns.length > 6 ? 'many-columns' : ''}`}>
        {columns.map((col) => (
          <div
            key={col.accessor}
            className="header-cell"
            onClick={() => handleSort(col.accessor)}
          >
            {col.header} {renderSortIcon(col.accessor)}

            {sortConfig && sortConfig.key === col.accessor && (
              <button
                className="clear-sort-icon"
                onClick={(e) => {
                  e.stopPropagation(); // Prevent sort toggle
                  setSortConfig(null); // Clear sorting
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
      </div>

      {sortedData.length === 0 ? (
        <p className="text-center text-muted py-3">No data available</p>
      ) : (
        sortedData.map((row, idx) => (
          <div key={idx} className="row-card">
            <div className={`row-card-content ${columns.length > 6 ? 'many-columns' : ''}`}>
              {columns.map((col) => (
                <div key={col.accessor} className="row-field">
                  <div className="row-field-label">{col.header}</div>
                  <div className="row-field-value">{row[col.accessor]}</div>
                </div>
              ))}
            </div>
          </div>
        ))
      )}
    </div>
  );
}

export default DataTable;
