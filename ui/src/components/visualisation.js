import React from 'react'
import FootballField from './footballField'

const Visualisation = () => {
    var footballFields = new Array(100);
    for (let index = 0; index < footballFields.length; index++) {
        footballFields[index] = 1
    }

    return <div>
        {
            footballFields.map(() => { return <FootballField /> })
        }
    </div>

}

export default Visualisation;