function MeasurementSelector({ onSelect }) {
  const measurements = ["BMI", "Blood Pressure", "Cholesterol"]; // stub list

  return (
    <div>
      <label>Measurement:</label>
      <select onChange={(e) => onSelect(e.target.value)}>
        <option value="">Select measurement</option>
        {measurements.map((m) => (
          <option key={m} value={m}>
            {m}
          </option>
        ))}
      </select>
    </div>
  );
}
export default MeasurementSelector;
