import React, { useState } from 'react';
import { FaSort, FaSortUp, FaSortDown, FaTimes } from 'react-icons/fa';
import 'bootstrap/dist/css/bootstrap.min.css';
import '../styles/dataTable.css';

const DataTable = ({ columns, data, globalFilter }) => {
  const [sortConfig, setSortConfig] = useState(null);

  const filteredData = data.filter((row) =>
    Object.values(row).join(' ').toLowerCase().includes(globalFilter.toLowerCase())
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

  const columnGridStyle = {
    gridTemplateColumns: `repeat(${columns.length}, minmax(150px, 1fr))`,
  };

  return (
    <div className="container-fluid">
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
            <p className="text-center text-muted py-3">No data available</p>
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

export default DataTable

// import React, { useState } from 'react';
// import { FaSort, FaSortUp, FaSortDown, FaTimes } from 'react-icons/fa';
// import '../styles/dataTable.css';

// const DataTable = ({ columns, data, globalFilter }) => {
//   const [sortConfig, setSortConfig] = useState(null);

//   const filteredData = data.filter((row) =>
//     Object.values(row)
//       .join(' ')
//       .toLowerCase()
//       .includes(globalFilter.toLowerCase())
//   );

//   const sortedData = React.useMemo(() => {
//     if (!sortConfig) return filteredData;
//     const { key, direction } = sortConfig;
//     return [...filteredData].sort((a, b) => {
//       const aVal = a[key];
//       const bVal = b[key];
//       if (aVal < bVal) return direction === 'asc' ? -1 : 1;
//       if (aVal > bVal) return direction === 'asc' ? 1 : -1;
//       return 0;
//     });
//   }, [filteredData, sortConfig]);

//   const handleSort = (key) => {
//     setSortConfig((prev) => {
//       if (!prev || prev.key !== key) return { key, direction: 'asc' };
//       return {
//         key,
//         direction: prev.direction === 'asc' ? 'desc' : 'asc',
//       };
//     });
//   };

//   const renderSortIcon = (key) => {
//     if (!sortConfig || sortConfig.key !== key) return <FaSort />;
//     return sortConfig.direction === 'asc' ? <FaSortUp /> : <FaSortDown />;
//   };

//   return (
//     <div className="data-table-container">
//       <div className="scroll-container">
//         <div
//           className="table-grid"
//           style={{ gridTemplateColumns: `repeat(${columns.length}, minmax(150px, 1fr))` }}
//         >
//           {/* Header Row */}
//           {columns.map((col) => (
//             <div
//               key={col.accessor}
//               className="header-cell"
//               onClick={() => handleSort(col.accessor)}
//             >
//               {col.header} {renderSortIcon(col.accessor)}
//               {sortConfig && sortConfig.key === col.accessor && (
//                 <button
//                   className="clear-sort-icon"
//                   onClick={(e) => {
//                     e.stopPropagation();
//                     setSortConfig(null);
//                   }}
//                   title="Clear sorting"
//                   aria-label={`Clear sorting on ${col.header}`}
//                   type="button"
//                 >
//                   <FaTimes />
//                 </button>
//               )}
//             </div>
//           ))}

//           {/* Data Rows */}
//           {sortedData.length === 0 ? (
//             <p className="text-center text-muted py-3">No data available</p>
//           ) : (
//             sortedData.map((row, idx) => (
//               <div key={idx} className="row-card" style={{ gridColumn: `span ${columns.length}` }}>
//                 <div
//                   className="row-card-grid"
//                   style={{ gridTemplateColumns: `repeat(${columns.length}, minmax(150px, 1fr))` }}
//                 >
//                   {columns.map((col) => (
//                     <div key={col.accessor} className="row-cell">
//                       <div className="row-field-value">{row[col.accessor]}</div>
//                     </div>
//                   ))}
//                 </div>
//               </div>
//             ))
//           )}
//         </div>
//       </div>
//     </div>
//   );
// }

// export default DataTable;
