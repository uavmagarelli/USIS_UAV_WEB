// Conduit Calculator
function calculateTotal()
{
  let unit_diameter={
    cable_one: 0.0370,
    cable_two: 0.0143,
    cable_three: 0.0189,
    cable_four: 0.0546,
    cable_five: 0.0346,
    cable_six: 0.0266,
    cable_seven: 0.0196,
    cable_eight: 0.0380,
    cable_nine: 0.0603,
    cable_ten: 0.0299,
    cable_eleven: 0.0908,
    cable_twelve: 0.0731,
    cable_thirteen: 0.0957,
    cable_fourteen: 0.0441,
  };
  let item_diameter={}

  item_diameter.cable_one = ($("#qty_cable_one").val() * unit_diameter.cable_one )
  $("#diameter_cable_one").val(item_diameter.cable_one);

  item_diameter.cable_two = ($("#qty_cable_two").val() * unit_diameter.cable_two )
  $("#diameter_cable_two").val(item_diameter.cable_two);

  item_diameter.cable_three = ($("#qty_cable_three").val() * unit_diameter.cable_three )
  $("#diameter_cable_three").val(item_diameter.cable_three);

  item_diameter.cable_four = ($("#qty_cable_four").val() * unit_diameter.cable_four )
  $("#diameter_cable_four").val(item_diameter.cable_four);

  item_diameter.cable_five = ($("#qty_cable_five").val() * unit_diameter.cable_five )
  $("#diameter_cable_five").val(item_diameter.cable_five);

  item_diameter.cable_six = ($("#qty_cable_six").val() * unit_diameter.cable_six )
  $("#diameter_cable_six").val(item_diameter.cable_six);

  item_diameter.cable_seven = ($("#qty_cable_seven").val() * unit_diameter.cable_seven )
  $("#diameter_cable_seven").val(item_diameter.cable_seven);

  item_diameter.cable_eight = ($("#qty_cable_eight").val() * unit_diameter.cable_eight )
  $("#diameter_cable_eight").val(item_diameter.cable_eight);

  item_diameter.cable_nine = ($("#qty_cable_nine").val() * unit_diameter.cable_nine )
  $("#diameter_cable_nine").val(item_diameter.cable_nine);

  item_diameter.cable_ten = ($("#qty_cable_ten").val() * unit_diameter.cable_ten )
  $("#diameter_cable_ten").val(item_diameter.cable_ten);

  item_diameter.cable_eleven = ($("#qty_cable_eleven").val() * unit_diameter.cable_eleven )
  $("#diameter_cable_eleven").val(item_diameter.cable_eleven);

  item_diameter.cable_twelve = ($("#qty_cable_twelve").val() * unit_diameter.cable_twelve )
  $("#diameter_cable_twelve").val(item_diameter.cable_twelve);

  item_diameter.cable_thirteen = ($("#qty_cable_thirteen").val() * unit_diameter.cable_thirteen )
  $("#diameter_cable_thirteen").val(item_diameter.cable_thirteen);

  item_diameter.cable_fourteen = ($("#qty_cable_fourteen").val() * unit_diameter.cable_fourteen )
  $("#diameter_cable_fourteen").val(item_diameter.cable_fourteen);

  let total = item_diameter.cable_one + item_diameter.cable_two + item_diameter.cable_three + item_diameter.cable_four
   + item_diameter.cable_five + item_diameter.cable_six + item_diameter.cable_seven + item_diameter.cable_eight
    + item_diameter.cable_nine + item_diameter.cable_ten + item_diameter.cable_eleven + item_diameter.cable_twelve
     + item_diameter.cable_thirteen + item_diameter.cable_fourteen;

  $("#total_value").text(total);

  let conduit = (total * 100)/40;
  $("#conduit_size").text(conduit);

}

$(function()
 {
    $(".qty").on("change keyup",calculateTotal);
})

// Wire Loss Calculations Lazy Version Watts
function calculateSystemLoad1()
{
//Transfer from html to java
    var cable_gauge = $("#cable_gauge").val() *1;
    var cable_run = $("#cable_run").val() *1;
    var amp_watts = $("#amp_watts").val() *1;
    var amp_taps_volts = $("#amp_taps_volts").val() *1;
    var amp_taps_ohms = $("#amp_taps_ohms").val() *1;

//Fixed for Copper Cabling
    var copper_K = 10.4;
//AWG Gauge Mill Diameter conversions
    if(cable_gauge == 1){
        var copper_diameter_mill = 289.3
    }
    if(cable_gauge == 2){
        var copper_diameter_mill = 257.6
    }
    if(cable_gauge == 3){
        var copper_diameter_mill = 229.4
    }
    if(cable_gauge == 4){
        var copper_diameter_mill = 204.3
    }
    if(cable_gauge == 5){
        var copper_diameter_mill = 181.9
    }
    if(cable_gauge == 6){
        var copper_diameter_mill = 162.0
    }
    if(cable_gauge == 7){
        var copper_diameter_mill = 144.3
    }
    if(cable_gauge == 8){
        var copper_diameter_mill = 128.5
    }
    if(cable_gauge == 9){
        var copper_diameter_mill = 114.4
    }
    if(cable_gauge == 10){
        var copper_diameter_mill = 101.9
    }
    if(cable_gauge == 11){
        var copper_diameter_mill = 90.74
    }
    if(cable_gauge == 12){
        var copper_diameter_mill = 80.81
    }
    if(cable_gauge == 13){
        var copper_diameter_mill = 71.96
    }
    if(cable_gauge == 14){
        var copper_diameter_mill = 64.08
    }
    if(cable_gauge == 15){
        var copper_diameter_mill = 57.07
    }
    if(cable_gauge == 16){
        var copper_diameter_mill = 50.82
    }
    if(cable_gauge == 17){
        var copper_diameter_mill = 45.26
    }
    if(cable_gauge == 18){
        var copper_diameter_mill = 40.30
    }
    if(cable_gauge == 19){
        var copper_diameter_mill = 35.89
    }
    if(cable_gauge == 20){
        var copper_diameter_mill = 31.96
    }
    if(cable_gauge == 21){
        var copper_diameter_mill = 28.46
    }
    if(cable_gauge == 22){
        var copper_diameter_mill = 25.35
    }
    if(cable_gauge == 23){
        var copper_diameter_mill = 22.57
    }
    if(cable_gauge == 24){
        var copper_diameter_mill = 20.10
    }
    if(cable_gauge == 25){
        var copper_diameter_mill = 17.90
    }
    if(cable_gauge == 26){
        var copper_diameter_mill = 15.94
    }
    if(cable_gauge == 27){
        var copper_diameter_mill = 14.20
    }
    if(cable_gauge == 28){
        var copper_diameter_mill = 12.64
    }
    if(cable_gauge == 29){
        var copper_diameter_mill = 11.26
    }
    if(cable_gauge == 30){
        var copper_diameter_mill = 10.03
    }
    if(cable_gauge == 31){
        var copper_diameter_mill = 8.928
    }
    if(cable_gauge == 32){
        var copper_diameter_mill = 7.950
    }
    if(cable_gauge == 33){
        var copper_diameter_mill = 7.080
    }
    if(cable_gauge == 34){
        var copper_diameter_mill = 6.305
    }
    if(cable_gauge == 35){
        var copper_diameter_mill = 5.615
    }
    if(cable_gauge == 36){
        var copper_diameter_mill = 5.000
    }
    if(cable_gauge == 37){
        var copper_diameter_mill = 4.453
    }
    if(cable_gauge == 38){
        var copper_diameter_mill = 3.965
    }
    if(cable_gauge == 39){
        var copper_diameter_mill = 3.531
    }
    if(cable_gauge == 40){
        var copper_diameter_mill = 3.134
    }
    if(cable_gauge == 41){
        var copper_diameter_mill = 2.75
    }
    if(cable_gauge == 42){
        var copper_diameter_mill = 2.50
    }
    if(cable_gauge == 43){
        var copper_diameter_mill = 2.25
    }
    if(cable_gauge == 44){
        var copper_diameter_mill = 2.00
    }
//The math equations
    var wireSystemLoad =  cable_gauge + cable_run;
    var systemWireLoadResistance = (copper_K*(2*cable_run)/(copper_diameter_mill*copper_diameter_mill));

// AMPLIFIER VOLTAGE
    if(amp_taps_ohms > 0)
        {
            $("#systemAmpLoadImp").text(amp_taps_ohms);
            $("#systemAmpLoadImp2").text(amp_taps_ohms);
            $("#systemAmpLoadImp3").text(amp_taps_ohms);
            $("#systemAmpLoadImp4").text(amp_taps_ohms);
            var ohm_amp_voltage = Math.sqrt(amp_taps_ohms*amp_watts);
            $("#systemAmpLoadVolt").text(ohm_amp_voltage);
            $("#systemAmpVoltage").text(ohm_amp_voltage);
            $("#systemAmpImp").text(amp_taps_ohms);
            $("#systemAmpPwr").text(amp_watts);
            var systemAmpCur = Math.sqrt(amp_watts/amp_taps_ohms);
            $("#systemAmpCur").text(systemAmpCur);
            var systemPwrFromAmp_temp = (ohm_amp_voltage*ohm_amp_voltage)/(amp_taps_ohms+systemWireLoadResistance);
            $("#systemPwrFromAmp").text(systemPwrFromAmp_temp);
            $("#systemAmpVoltage2").text(ohm_amp_voltage);
            $("#systemPwrFromAmp2").text(systemPwrFromAmp_temp);
            $("#systemLoad").text(systemWireLoadResistance+amp_taps_ohms);
            var system_current_p1 = (systemWireLoadResistance+amp_taps_ohms);
            var system_Current = Math.sqrt(systemPwrFromAmp_temp/system_current_p1);
            $("#systemCurrent").text(system_Current);
            $("#systemCurrent2").text(system_Current);
            var systemAvailPwr = (system_Current*system_Current)*amp_taps_ohms;
            $("#systemAvailPwr").text(systemAvailPwr);
        }
        else
        {
            var systemAmpLoadImp = ((amp_taps_volts * amp_taps_volts)/amp_watts);
            $("#systemAmpLoadImp").text(systemAmpLoadImp);
            $("#systemAmpLoadImp2").text(systemAmpLoadImp);
            $("#systemAmpLoadImp3").text(systemAmpLoadImp);
            $("#systemAmpLoadImp4").text(systemAmpLoadImp);
            $("#systemAmpLoadVolt").text(amp_taps_volts);
            $("#systemAmpVoltage2").text(amp_taps_volts);
            var systemAmpCur = Math.sqrt(amp_watts/systemAmpLoadImp);
            $("#systemAmpCur").text(systemAmpCur);
            var systemPwrFromAmp = (amp_taps_volts*amp_taps_volts)/(systemAmpLoadImp+systemWireLoadResistance);
            $("#systemPwrFromAmp").text(systemPwrFromAmp);
            $("#systemPwrFromAmp2").text(systemPwrFromAmp)
            var systemLoad = systemWireLoadResistance+systemAmpLoadImp;
            $("#systemLoad").text(systemLoad);
            var system_Current = Math.sqrt(systemPwrFromAmp/systemLoad);
            $("#systemCurrent").text(system_Current);
            $("#systemCurrent2").text(system_Current);
            var systemAvailPwr = (system_Current*system_Current)*systemAmpLoadImp;
            $("#systemAvailPwr").text(systemAvailPwr);
        }

//Mapping Answers Back to HTML
    $("#available_watts").text(systemAvailPwr);
    $("#systemWireLoadResistance").text(systemWireLoadResistance);
    $("#systemWireLoadResistanceCMF").text(copper_K);
    $("#systemWireRunDistance").text(cable_run);
    $("#systemWireDiameterMills").text(copper_diameter_mill);
    $("#systemAmpLoadPwr").text(amp_watts);
    $("#systemAmpPwrRate").text(amp_watts);
    $("#systemPwrFromAmpWireLoad").text(systemWireLoadResistance);

}

$(function()
 {
    $("#cable_gauge").on("change keyup",calculateSystemLoad1);
    $("#cable_run").on("change keyup",calculateSystemLoad1);
    $("#amp_watts").on("change keyup",calculateSystemLoad1);
    $("#amp_taps_volts").on("change keyup",calculateSystemLoad1);
    $("#amp_taps_ohms").on("change keyup",calculateSystemLoad1);
})

// Ohms Speaker Impedance - Parallel
function calculateOhmSpkrImpPar()
{
    var spkr_one = $("#sp1_ohms_imp_p_value").val() *1;
    var spkr_two = $("#sp2_ohms_imp_p_value").val() *1;

    if (spkr_one == spkr_two)
    {
    var matching_total = spkr_one/2;
    $("#ohms_imp_p_total").text(matching_total);
    }
    else
    {
    var temp_1 = (spkr_one*spkr_two);
    var temp_2 = temp_1/(spkr_one+spkr_two);
    $("#ohms_imp_p_total").text(temp_2);
    }
}

$(function()
 {
    $("#sp1_ohms_imp_p_value").on("change keyup",calculateOhmSpkrImpPar);
    $("#sp2_ohms_imp_p_value").on("change keyup",calculateOhmSpkrImpPar);
})

// Ohms Speaker Impedance - Series
function calculateOhmSpkrImpSer()
{
    var spkr_one = $("#sp1_ohms_imp_s_value").val() *1;
    var spkr_two = $("#sp2_ohms_imp_s_value").val() *1;
    var temp = spkr_one + spkr_two;
    $("#ohms_imp_s_total").text(temp);
}

$(function()
 {
    $("#sp1_ohms_imp_s_value").on("change keyup",calculateOhmSpkrImpSer);
    $("#sp2_ohms_imp_s_value").on("change keyup",calculateOhmSpkrImpSer);
})

// Volt Speaker Impedance - Parallel
function calculateVoltSpkrImpPar()
{
    var tap_volts_p_value = $("#tap_volts_p_value").val() *1;
    var quantity_volts_imp_p_value = $("#quantity_volts_imp_p_value").val() *1;
    var ampvolts_volts_imp_p_value = $("#ampvolts_volts_imp_p_value").val() *1;

    var min_power = tap_volts_p_value*quantity_volts_imp_p_value;
    $("#volts_power_p_total").text(min_power);

    var Power_headroom = ((min_power/100)*25) + min_power;
    $("#volts_power_p_total_headroom").text(Power_headroom);

    var impdeance = (ampvolts_volts_imp_p_value*ampvolts_volts_imp_p_value)/min_power;
    $("#volts_impedance_p_total").text(impdeance);
}

$(function()
 {
    $("#tap_volts_p_value").on("change keyup",calculateVoltSpkrImpPar);
    $("#quantity_volts_imp_p_value").on("change keyup",calculateVoltSpkrImpPar);
    $("#ampvolts_volts_imp_p_value").on("change keyup",calculateVoltSpkrImpPar);
})

// Btu/Hr Calc
function btuCalculation()
{
    var watts = $("#watts").val() *1;
    $("#btutotal").text(watts*3.4);
}

$(function()
 {
    $("#watts").on("change keyup",btuCalculation);
})

// Speaker Diameter Coverage
function spkrdiameterCalculation()
{
    var ceilingheight = $("#ceilingheight").val() *1;
    var coverageangle = $("#coverageangle").val() *1;
    var temp_1 = 2*(ceilingheight-48);
    var temp_2 = Math.tan(coverageangle / 2)
    $("#coveragetotal something ").text(temp_1*temp_2);
}

$(function()
 {
    $("#ceilingheight").on("change keyup",spkrdiameterCalculation);
    $("#coverageangle").on("change keyup",spkrdiameterCalculation);
})