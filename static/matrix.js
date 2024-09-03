let mycontainer = document.getElementById("circuitData");
console.log("Fetched element Sucessfully", mycontainer);
function handleSubmit() {
  const dataTable = document.getElementById("dataTable");
  const matrix = [];
  let matrixString = ""; // Variable to store the string representation of the matrix

  // Iterate over each row in dataTable
  dataTable.querySelectorAll("tr").forEach((row, rowIndex) => {
    const rowData = [];
    let highestFilledIndex = -1; // Track the highest filled index in the current row
    let maxFilledIndex = -1; // Track the maximum index of filled cells in the current row

    // Check if the row contains .gateWire class
    const hasGateWire = row.classList.contains("gateWire");

    // Iterate over each cell in the row
    row.querySelectorAll("td").forEach((cell, index) => {
      // Check if the cell is filled
      const isCellFilled = cell.children.length > 0;

      if (isCellFilled) {
        // Update the highestFilledIndex if the current index is greater than the current highestFilledIndex
        highestFilledIndex = Math.max(highestFilledIndex, index);
        // Update the maxFilledIndex with the current index
        maxFilledIndex = index;

        // Get the ID (text) of the image in the cell
        const imageId = cell.firstElementChild.id;
        rowData.push(imageId);
      } else {
        // If the row contains .gateWire class and the current index matches the next row's index, put 'X'
        if (hasGateWire && rowIndex + 1 < dataTable.rows.length) {
          const nextRow = dataTable.rows[rowIndex + 1];
          const nextCell = nextRow.cells[index];
          if (nextCell.children.length > 0) {
            rowData.push("X");
          } else {
            // Fill with "I" if no "X" is present in the next row
            rowData.push("I");
          }
        } else {
          // If the cell is empty and its index is less than or equal to the highestFilledIndex, push "I"
          if (index <= highestFilledIndex) {
            rowData.push("I");
          } else {
            // If the cell is empty and its index is greater than the highestFilledIndex, fill it with "I"
            rowData.push("I");
          }
        }
      }
    });

    // Push the row data to the matrix if there's any content
    if (rowData.length > 0) {
      // Reduce the size of the row matrix up to the last filled cell
      matrix.push(rowData.slice(0, maxFilledIndex + 1));
    }

    // Print the maxFilledIndex for each row
    console.log(`Max filled index in row ${row.id}: ${maxFilledIndex + 1}`);
  });

  // If the matrix is empty after processing all rows or only contains empty rows, print a message to the console
  if (
    matrix.length === 0 ||
    matrix.every((row) => row.every((cell) => cell === ""))
  ) {
    console.log("No circuit is designed yet");
    return; // Exit the function early
  }

  // Generate the string representation of the matrix
  matrixString = matrix.map((row) => "[ " + row.join("  , ") + " ]").join("\n");

  // Print the generated matrix string to console for testing
  console.log("Matrix:");
  console.log(matrixString);
  mycontainer.innerText = matrixString;

  // Print the number of rows with content
  console.log("Number of rows with content: " + matrix.length);
}
