import React, { useEffect, useState } from 'react';
import { DataGrid, GridColDef, GridValueGetterParams } from '@mui/x-data-grid';

const columns: GridColDef[] = [
  { field: 'id', headerName: 'ID', width: 230 },
  { field: 'firstName', headerName: 'First name', width: 130 },
  { field: 'LastName', headerName: 'Last name', width: 130 },
  {
    field: 'YearOfExperience',
    headerName: 'year of experience',
    type: 'number',
    width: 200,
  }
];

const CandidTable= () => {
const [rows, setRows] = useState([]);
const loadCandidat = async () => {
   const response = await fetch('/get_candidats',{
                headers: {
                  "Content-Type": "application/json",
                },
                method: "get",
              });
            if (response.ok) {
                    // if HTTP-status is 200-299
                    // get the response body (the method explained below)
                   const json = await response.json();
                   console.log('sent '+ json)
                   setRows(json)

                 }
            else {
                   alert("HTTP-Error: " + response.status);
                  }
    };
     useEffect(() => {
    loadCandidat();
  }, []);
  return (
    <div style={{ height: 400, width: '100%' }}>
      <DataGrid
        rows={rows}
        columns={columns}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
      />
    </div>
  );
}
export default CandidTable