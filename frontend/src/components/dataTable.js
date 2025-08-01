import React from 'react';

function DataTable({ columns, data }) {
  return (
    <table className="data-table" style={{ width: '100%', borderCollapse: 'collapse' }}>
      <thead>
        <tr>
          {columns.map(col => (
            <th
              key={col.accessor}
              style={{ borderBottom: '2px solid #ccc', padding: '8px', textAlign: 'left' }}
            >
              {col.header}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.length === 0 ? (
          <tr>
            <td colSpan={columns.length} style={{ padding: '8px', textAlign: 'center' }}>
              No data available
            </td>
          </tr>
        ) : (
          data.map((row, rowIndex) => (
            <tr key={rowIndex} style={{ borderBottom: '1px solid #eee' }}>
              {columns.map(col => (
                <td key={col.accessor} style={{ padding: '8px' }}>
                  {row[col.accessor]}
                </td>
              ))}
            </tr>
          ))
        )}
      </tbody>
    </table>
  );
}

export default DataTable;
