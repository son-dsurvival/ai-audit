import pandas as pd
import numpy as np
import math

spec=pd.read_csv('pump_specs_static_3rows.csv')
table=pd.read_csv('pump_maintenance_timeseries_1000_rows.csv')

true={
      "ID":[],
      "date":[],
      "pressure":[],
      "flow_rate":[],
      "suction_pressure":[],
      "discharge_pressure":[],
      "rpm":[],
      "vibration_rms":[],
      "vibration_peak":[],
      "structural_vibration":[],
      "motor_current":[],
      "power_draw_kw":[],
      "bearing_temperature":[],
      "motor_temperature":[],
      "pump_casing_temperature":[],
      "oil_temperature":[],
      "fluid_temperature":[],
      "ambient_temperature":[],
      "oil_pressure":[],
      "oil_level":[],
      "seal_pressure":[],
      "leakage_rate":[],
      "runtime_hours_since_last_maintenance":[],
      "days_since_last_maintenance":[],
      "start_stop_count":[],
      "acoustic_signal_level":[],
      "time_until_next_maintenance":[]}

for index, row in table.iterrows():
    data=spec[spec['ID'] == row['ID']].iloc[0]
    true["ID"].append(row['ID'])
    true["date"].append(row['date'])
    pressure= row["pressure"]/(data["rho"]*9.8*data["Hr"])
    true["pressure"].append(pressure)
    flow= row["flow_rate"]/data["Q"]
    true["flow_rate"].append(flow)
    suction_pressure= row["suction_pressure"]/(data["Ps"])
    true["suction_pressure"].append(suction_pressure)
    discharge_pressure= row["discharge_pressure"]/(data["Pd"])
    true["discharge_pressure"].append(discharge_pressure)
    rpm= row["rpm"]/data["N"]
    true["rpm"].append(rpm)
    vibration_rms= row["vibration_rms"]/data["Vrms"]
    true["vibration_rms"].append(vibration_rms)
    vibration_peak= row["vibration_peak"]/data["Vpeak"]
    true["vibration_peak"].append(vibration_peak)
    structural_vibration= row["structural_vibration"]/data["Vstruct"]
    true["structural_vibration"].append(structural_vibration)
    motor_current= row["motor_current"]*math.sqrt(3)*data["V_r"]*data["PF"]/(data["P_motor_r"]* 1000)
    true["motor_current"].append(motor_current)
    power_draw_kw= row["power_draw_kw"]*data["eta_pump"]*data["eta_motor"]/pressure*flow
    true["power_draw_kw"].append(power_draw_kw)
    b_temp= (row["bearing_temperature"]-row["ambient_temperature"])/(data["T_bearing"]-row["ambient_temperature"])
    true["bearing_temperature"].append(b_temp)
    m_temp= (row["motor_temperature"]-row["ambient_temperature"])/(data["T_motor"]-row["ambient_temperature"])
    true["motor_temperature"].append(m_temp)
    p_temp= (row["pump_casing_temperature"]-row["ambient_temperature"])/(data["T_casing"]-row["ambient_temperature"])
    true["pump_casing_temperature"].append(p_temp)
    o_temp= (row["oil_temperature"]-row["ambient_temperature"])/(data["T_oil"]-row["ambient_temperature"])
    true["oil_temperature"].append(o_temp)
    f_temp= row["fluid_temperature"]/data["T_fluid"]
    true["fluid_temperature"].append(f_temp)
    true["ambient_temperature"].append(row['ambient_temperature'])
    oil_pressure= row["oil_pressure"]/data["P_oil"]
    true["oil_pressure"].append(oil_pressure)
    oil_level= row["oil_level"]/data["Level_oil"]
    true["oil_level"].append(oil_level)
    seal_pressure= row["seal_pressure"]/data["P_seal"]
    true["seal_pressure"].append(seal_pressure)
    leakage_rate= row["leakage_rate"]/data["Leakage"]
    true["leakage_rate"].append(leakage_rate)
    runtime_hours= row["runtime_hours_since_last_maintenance"]/data["Runtime_since_maintenance"]
    true["runtime_hours_since_last_maintenance"].append(runtime_hours)
    days_since_maintenance= row["days_since_last_maintenance"]/data["Days_since_maintenance"]
    true["days_since_last_maintenance"].append(days_since_maintenance)
    start_stop_count= row["start_stop_count"]/data["StartStop_allowed"]
    true["start_stop_count"].append(start_stop_count)
    acustic= row["acoustic_signal_level"]/data["Acoustic_actual"]
    true["acoustic_signal_level"].append(acustic)
    true["time_until_next_maintenance"].append(row['time_until_next_maintenance'])
cleaned_data=pd.DataFrame(true)
cleaned_data.to_csv('cleaned_pump_data.csv', index=False)