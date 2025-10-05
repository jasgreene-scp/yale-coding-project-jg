function DiseaseSelector({ onSelect }) {
  const diseases = ["Cancer", "Diabetes", "Asthma"]; // stub list

  return (
    <div>
      <label>Disease:</label>
      <select onChange={(e) => onSelect(e.target.value)}>
        <option value="">Select disease</option>
        {diseases.map((d) => (
          <option key={d} value={d}>
            {d}
          </option>
        ))}
      </select>
    </div>
  );
}
export default DiseaseSelector;
