import React from 'react'
import Typography from '@mui/material/Typography';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';
import Grid from '@mui/material/Grid';

class Form extends React.Component {

constructor(props) {
     super(props)
     this.state = {
         prenom : "",
         nom : "",
         year_xp : 0
        };
     this.insert = this.insert.bind(this);
     this._handleNomField = this._handleNomField.bind(this);
     this._handlePrenomField =  this._handlePrenomField.bind(this);
     this._handleExperienceField =  this._handleExperienceField.bind(this);
      };

_handleExperienceField= (e)=>{ this.setState({  year_xp : e.target.value });}
_handleNomField=(e)=>
{ this.setState({  nom : e.target.value });}
_handlePrenomField=(e)=>
{ this.setState({  prenom : e.target.value });}

async insert()
    {
        const state_JSON = JSON.stringify(
        {'nom': this.state.nom, 'prenom': this.state.prenom, 'year_of_experience': this.state.year_xp});
         const response = await fetch('/add_candidat',{
                headers: {
                  "Content-Type": "application/json",
                },
                method: "POST",
                body: state_JSON,
              });
              console.log(state_JSON)
            if (response.ok) {
                    // if HTTP-status is 200-299
                    // get the response body (the method explained below)
                   const json = await response.json();
                   console.log('sent '+ json)
                 }
            else {
                   alert("HTTP-Error: " + response.status);
                  }
    };
render()
{  const {classes} = this.props
   return(
        <div>

         <Grid container spacing={3} style={{ padding:20}}>
             <Grid item xs={12} sm={4}>
                <TextField required id="outlined-number" label="nom"  InputLabelProps={{shrink: true,}} onChange={this._handleNomField} variant="outlined"/>             </Grid>
              <Grid item xs={12} sm={4}>
                <TextField required id="outlined-number" label="prenom" InputLabelProps={{shrink: true,}} onChange={this._handlePrenomField} variant="outlined"/>

             </Grid>
               <Grid item xs={12} sm={4}>
                <TextField required id="outlined-number" label="experience" type="number" InputLabelProps={{shrink: true,}} onChange={this._handleExperienceField} variant="outlined"/>

             </Grid>

         </Grid>
         <Button variant='outlined' component="span" onClick={this.insert} style={{left:300,marginBottom:10,background:'#C3C2DA',}}>
                               Ajouter candidatures
         </Button>


        </div>


   );


}

}
export default Form