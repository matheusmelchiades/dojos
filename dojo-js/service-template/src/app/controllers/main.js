
module.exports.get = (req, res) => {

    try {

        return res.json({ status: 'running' })

    } catch (err) {
        console.log(err)

        return err
    }
}
