const app = require('./app/index')
const database = require('./datatbase')

database.connect()

app.listen(3333, () => {
    console.log('server running')
})
