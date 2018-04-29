# PushFin

## Setup

1. Install pushfin: `pip3 install pushfin`
2. Create configuration file at: `~/.pushfin.yaml`. Take a look at the [example configuration](https://github.com/stv0g/pushfin/blob/master/etc/pushfin.yaml).
3. Add pushfin to crontab: `crontab -e`:

```
12 * * * * pushfin
````

## Transaction fields for formatting

### MT940

Standard transaction data is parsed by the [`mt940` Python Module](https://github.com/WoLpH/mt940).

Common fields are listed below:

| Formatting field				| Example value | Description |
| :--						| :-- | :-- |
| `trx[status]`					| 'D' | 'D' = Debit, 'C' = Credit |
| `trx[funds_code]`				| None |
| `trx[id]`					| 'NMSC' |
| `trx[customer_reference]`			| None |
| `trx[bank_reference]`				| None |
| `trx[extra_details]`				| '' |
| `trx[currency]`				| 'EUR' |
| `trx[date]`					| | Unix Timestamp |
| `trx[entry_date]`				| | Unix Timestamp |
| `trx[transaction_code]`			| '020' |
| `trx[posting_text]`				| 'Überweisung' |
| `trx[prima_nota]`				| '006200' |
| `trx[purpose]`				| 'Kino Tickets' |
| `trx[applicant_bin]`				| 'PBNABSEEFXXX' |
| `trx[applicant_iban]`				| 'DE71235623523523523' |
| `trx[applicant_name]`				| 'Max Mustermann' |
| `trx[return_debit_notes]`			| None |
| `trx[recipient_name]`				| None |
| `trx[additional_purpose]`			| None |
| `trx[gvc_applicant_iban]`			| None |
| `trx[gvc_applicant_bin]`			| None |
| `trx[end_to_end_reference]`			| None |
| `trx[additional_position_reference]`		| None |
| `trx[applicant_creditor_id]`			| None |
| `trx[purpose_code]`				| None |
| `trx[additional_position_date]`		| None |
| `trx[deviate_applicant]`			| None |
| `trx[deviate_recipient]`			| None |
| `trx[FRST_ONE_OFF_RECC]`			| None |
| `trx[old_SEPA_CI]`				| None |
| `trx[old_SEPA_additional_position_reference]` | None |
| `trx[settlement_tag]`				| None |
| `trx[debitor_identifier]`			| None |
| `trx[compensation_amount]`			| None |
| `trx[original_amount]`			| None |

### Extra fields

For ease formatting, we extended the standard MT940 fields with the following helpers:

| Formatting field				| Example value | Description |
| :--						| :-- | :-- |
| `trx[date_ts]`				| 1525007188	| A Unix timestamp of the `date` field |
| `trx[date_fmt]`				| '2018-04-28'	| A formatted date of the `date` field |
| `trx[entry_date_ts]`				| 1525007188	| A Unix timestamp of the `entry_date` field |
| `trx[entry_date_fmt]`				| '2018-04-28'	| A formatted date of the `entry_date` field |
| `trx[amout]`					| -20.42	| Just the amount of the transaction (see `amount`) |
| `trx[dir]`					| 'from'/'to'	| |
| `trx[color]`					| '#009933'	| |
| `bal[amount]`					| '3.52'	| |
| `bal[currency]`				| 'EUR'		| Current balance valuta |
| `bal[date]`					| '2018-03-23'	| Balance currency |
| `bal[date_fmt]`				|		| Date of last valuta |
